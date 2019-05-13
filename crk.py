class WaterMarkUtils:

    def __do_something(self):
        pass

    def removewater_mark(self, input_file_path, output_path):
        self.__do_something()
        return output_path + "/abc.mp4"


if __name__ == "__main__":
    water_mark = WaterMarkUtils()
    water_mark.removewater_mark("/tmp/a.mp4", "/tmp/")

