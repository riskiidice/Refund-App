import uplink

class THSMS(uplink.Consumer):
    @uplink.get("/api/rest")
    def send_params(self, **params:uplink.QueryMap)
