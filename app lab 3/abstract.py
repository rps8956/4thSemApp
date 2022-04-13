import abc
class startup(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def discussion(self):
        pass
class infra_work_area(startup):
    def discussion(self):
        print("The infrastructure of work area would include an office space spanning 6000 sf containing "
                "at least 4 separate chambers and 2 conferance halls to accomodate 20 employees initially. ")

class cap_and_fund(startup):
    def discussion(self):
        print("funding options:\nBootstraping\nCrowd funding\nAngel investment")

class human_resource(startup):
    def discussion(self):
        print("The startup would initially employ 20 well qualified indivisuals who are hardworking,passionate"
              "for the company's goal and confident.")

i = infra_work_area()
i.discussion()
c = cap_and_fund()
c.discussion()
h = human_resource()
h.discussion()