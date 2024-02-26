import psutil


class SpeedMeter:
    def __init__(self):
        self.prev_upload = psutil.net_io_counters().bytes_sent
        self.prev_download = psutil.net_io_counters().bytes_recv
        self.prev_total = 0
        self.now_upload = 0
        self.now_download = 0
        self.now_total = 0
        self.upload_speed = 0
        self.download_speed = 0
        self.total_speed = 0
        
        self.total_consume = 0

    def update(self):
        data = psutil.net_io_counters()
        self.now_upload = data.bytes_sent
        self.now_download = data.bytes_recv
        self.now_total = self.now_upload + self.now_download

        self.upload_speed = self.now_upload - self.prev_upload
        self.download_speed = self.now_download - self.prev_download
        self.total_speed = self.upload_speed + self.download_speed

        self.prev_upload = self.now_upload
        self.prev_download = self.now_download
        self.prev_total = self.now_total
        

    def convert_speed(self, value):
        return self.to_mb(value / 1024)


    def to_mb(self, kb):
        if kb < 1024:
            return f"{round(kb, 2)} KB"
        return self.to_gb(kb / 1024)

    def to_gb(self, mb):
        if mb < 1024:
            return f"{round(mb, 2)} MB"
        return f"{round(mb / 1024, 2)} GB"
