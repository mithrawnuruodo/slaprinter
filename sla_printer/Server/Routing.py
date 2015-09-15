__author__ = 'aslan'

import json
import os

from flask import Flask
from flask import render_template
from flask import request
from flask import Response

from Model import PrintingTaskData

#import sys
#import os
# set sytem path to be directory above so that a can be a
# package namespace
#DIRECTORY_SCRIPT = os.path.dirname(os.path.realpath(__file__))
#sys.path.insert(0,DIRECTORY_SCRIPT+"/..")

from Control.MessageHandler import Observable
from Control.Messages import QuitMessage

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__)) + "/Server"
TEMPLATE_DIR = PROJECT_DIR + '/templates'
STATIC_DIR = PROJECT_DIR +'/static'
#print("PROJECT_DIR : "+str(PROJECT_DIR))
#print("STATIC_DIR : "+str(STATIC_DIR))
#print("TEMPLATE_DIR :"+str(TEMPLATE_DIR))
#import Control as cntrl



class RoutingData(object):
    def __init__(self, args, kwargs):
        super(RoutingData, self).__init__()
        self.args = args
        self.kwargs = kwargs

def route(*args, **kwargs):
    def wrap(fn):
        l = getattr(fn, '_routing_data', [])
        l.append(RoutingData(args, kwargs))
        fn._routing_data = l
        return fn
    return wrap

class SlaPrinterAppProto(object):
    pass

class SlaPrinterApp(Flask, Observable):
    def __init__(self, import_name, db_controller = None, bus = None):
        #super(SlaPrinterApp, self).__init__(import_name, template_folder=TEMPLATE_DIR, static_url_path=STATIC_DIR)
        Flask.__init__(self,import_name, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)
        Observable.__init__(self, bus=bus)

        self.endpoint_prefix = None
        for name in dir(self):
            if hasattr(getattr(self, name), ("_routing_data")):
                fn = getattr(self, name)
                rds = fn._routing_data
                for rd in rds:
                    self.route(*rd.args, **rd.kwargs)(fn)


        self.register_error_handler(404, self.page_not_found)
        self.db_controller = db_controller


    @route("/")
    @route("/index")
    def index(self):

        #data = cntrl.PrintingTaskController()

        if self.db_controller is not None:
            tasks = self.db_controller.printing_tasks()
            active_job = self.db_controller.active_job()
            return render_template("index.html", printing_tasks = tasks, active_job= active_job)

        else:
            return render_template("index.html")

    @route("/enqueue")
    def enqueue(self):

        return render_template("enqueue.html")

    @route("/info")
    def info(self):

        return render_template("info.html")

    @route("/quit", methods = ['POST', 'GET'])
    def quit(self):


        #self.shutdown_server()

        msg = QuitMessage(SlaPrinterAppProto(),"sla printer shutting down")
        self.put_message(msg)

        return "quitting"

    @route("/post/raw/", methods = ['POST'])
    def post_data(self):
        '''
        function used to send simple raw string data to 3D printer

        :return: according success / fail message
        '''


        # get current data pool to store new objects
        #data_pool = cntrl.DataPool()

        # load data
        data = json.loads(request.data)


        # if "data" in data:
        #     d  = RawData(data["data"])
        #     data_pool.add(d)
        #     return str(d)
        # else:
        #     return "no data received"

    @route("/post/task/",  methods = ['POST'])
    def post_task(self):
        '''
        Function used to send printing task to 3D printer

        :return: according success / fail message
        '''

        # load data
        data = json.loads(request.data)

        # create empty printing task
        task = PrintingTaskData()

        # if received data parseable to task object store new printing task
        if task.parse(data):

            if self.db_controller is not None:
                jid = self.db_controller.save_printing_task(task)
                return json.dumps({"id": jid})
            else:
                return "no valid printing task received"
        else:
            return "invalid data"


    @route("/download/<tid>/",  methods = ['POST', 'GET'])
    def download_zip(self, tid):

        # data_pool = cntrl.DataPool()
        #
        #
        # task = data_pool.get_by_id(tid)
        #
        # if task is not None:
        #
        #     zip = task.stl_file
        #     zip = base64.decodestring(zip)
        #
        # else:
        zip = ''

        file_name = "bla"

        return Response(zip,
                mimetype='application/zip',
                #headers={'Content-Disposition':'attachment;filename=' + str(task.file_name) + '.zip'})
                headers={'Content-Disposition':'attachment;filename=' + str(file_name) + '.zip'})


    def page_not_found(self, e):
        return render_template('404.html'), 404

    def shutdown_server(self):
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()


if __name__ == "__main__":

    server =SlaPrinterApp(__name__)
    server.run(host='0.0.0.0',debug=True, port=4242,  use_evalex=False)