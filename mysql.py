import pymysql
import sys

# 功能：    更新数据库

argc = len(sys.argv)
if argc < 2:
    print('功能：    更新数据库')
    print('使用方法：update.py后面直接跟id，多个id之间用空格隔开。\n举例：\n  update.py 1 2');
    print()
else:
    try:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='jr2help',
                               charset='utf8')
        print('数据库链接成功！！！')
        print()
        print('开始更新任务状态...')
        # for i in range(1, argc):
        #     print("任务%d = %s" % (i, sys.argv[i]))
        #     t_ctrtask_sql = "update database.test set status = %d where id = '%s'"
        #     cur = conn.cursor()
        #     cur.execute(t_ctrtask_sql % (0, sys.argv[i]))
        #     cur.close()
        #     print("任务%d = %s更新成功！！！" % (i, sys.argv[i]))
        #     print()
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
    finally:
        print('执行结束，数据库链接关闭！！！')