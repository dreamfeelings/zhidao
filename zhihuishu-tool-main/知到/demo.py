# Author ：梦情
# Time ：2023/4/4 13:30
# File : demo.py
def gen_watch_point( start_time, end_time=300):
    """
    生成watchPoint（提交共享学分课视频进度接口用）
    :param start_time: 起始视频进度条时间，秒
    :param end_time: 提交时距离起始时间的间隔，秒。默认为正常观看时请求database接口的间隔时间
    """
    record_interval = 1990
    total_study_time_interval = 4990
    cache_interval = 180000
    database_interval = 300000
    watch_point = None
    total_stydy_time = start_time
    for i in range(int(end_time * 1000)):
        if i % total_study_time_interval == 0:
            total_stydy_time += 5
        if i % record_interval == 0 and i >= record_interval:
            t = int(total_stydy_time / 5) + 2
            if watch_point is None:
                watch_point = '0,1,'
            else:
                watch_point += ','
            watch_point += str(t)
    print(watch_point)
    return watch_point

gen_watch_point(1)