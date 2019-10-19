# import psutil


class StatsCollector(object):

    @classmethod
    def fetchstats(cls):
        # cpu = psutil.cpu_freq().max * psutil.cpu_count()
        # mem = round(psutil.virtual_memory().total / 1000000)
        # battery = psutil.sensors_battery().percent
        #
        # print("total max cpu freq: ", cpu)
        # print("memory: ", mem)
        # print("battery: ", battery)
        #
        # return cpu, mem, battery
        # else:
        #     return 0, 0, 0
        return 0, 0, 0
