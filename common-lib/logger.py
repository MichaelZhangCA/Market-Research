from repobase import MysqlConnection

class Logger(object):

    def __init__(self, action='- no named -', **kwargs):
        self.query = ("INSERT INTO `ops.operation_log` (`effective_date`, `service_name`, `action_type`, `severity`, `log_message`) "
                 "VALUES  ( current_date, '{0}', %s, %s, %s)".format(Logger.servicename))
        Logger.action = action

        return super().__init__(**kwargs)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    # setup service name and environment parameters
    def init_logger(env, servicename):
        Logger.env = env
        Logger.servicename = servicename


    def __get_log_sql(self):
        return self.query

    def __exec_log(self, serverity, action, msg):
        with MysqlConnection() as cnx:
            cur = cnx.cursor()

            # clear current record
            cur.execute(self.query, (action, serverity, msg))
            cnx.commit()
            cur.close()


    '''
    def loginfo(self,action,msg):
        self.__exec_log("I", action, msg)


    def logwarning(self,action,msg):
        self.__exec_log("W", action, msg)

    def logerror(self,action,msg):
        self.__exec_log("E", action, msg)
    '''

    def loginfo(self,msg):
        self.__exec_log("I", self.action, msg)


    def logwarning(self,msg):
        self.__exec_log("W", self.action, msg)

    def logerror(self,msg):
        self.__exec_log("E", self.action, msg)
