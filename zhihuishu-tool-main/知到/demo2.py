# Author ：梦情
# Time ：2023/4/4 18:01
# File : demo2.py
def submit_study_record(video_lesson, init_learn_time, dt, recruit_id, study_total_time, learning_token_id, course_id):
    print(f'当前视频：{video_lesson.lesson_name}, 视频总时长：{video_lesson.video_sec}, '
          f'\n上此观看到：{init_learn_time}, 本次需要观看：{dt}')
    watch_point = zhs_encrypt.gen_watch_point(init_learn_time, dt)
    small_lesson_id = 0
    if video_lesson.small_lesson_id:
        small_lesson_id = video_lesson.small_lesson_id
    last_view_id = course.query_user_recruit_id_last_video_id(recruit_id)['data']["lastViewVideoId"]
    # 提交时的学习时间相关（之前视频观看到的时间点加上dt）
    play_time = dt - (dt % 5)
    video_pos = time.strftime("%H:%M:%S", time.gmtime(init_learn_time + dt))
    # 生成ev
    evt = [recruit_id, video_lesson.lesson_id, small_lesson_id, last_view_id, video_lesson.chapter_id, "0",
           play_time, study_total_time, video_pos]
    ev = zhs_encrypt.get_ev(evt)
    resp = course.save_database_interval_time(watch_point, ev, learningTokenId=learning_token_id, courseId=course_id)
    print(resp)
    if not is_immediately_submit:
        time.sleep(dt)
    else:
        time.sleep(10)
    return resp