"""
    main_module - 时间转换测试，测试是将对应方法的@unittest.skip注释掉.

    Main members:

        # __main__ - 程序入口.
"""
import unittest
import sys

sys.path.insert(0, './')  # 定义搜索路径的优先顺序，序号从0开始，表示最大优先级

import time_convert  # noqa
print('time_convert module path :{}'.format(time_convert.__file__))  # 输出测试模块文件位置
from time_convert import TimeNormalizer  # noqa


class TestConvert(unittest.TestCase):
    """ 时间转换测试.

    Main methods:
        test_time_convert - 时间转换测试.
    """

    # @unittest.skip('debug')
    def test_time_convert(self):
        """ 时间转换测试.
        """
        print('{} test_time_convert {}'.format('-'*15, '-'*15))
        tc = TimeNormalizer(isPreferFuture=False)
        texts = [
            '三月',
            '今年三月',
            '三月中旬',
            '去年三月十五日',
            '去年六月份',
            '今天',
            '昨天下午三点',
            '一个月后',
            '明年'
        ]
        for text in texts:
            print('{}\t{}'.format(text, tc.parse(text)))
        """
        三月    {'key': '3月', 'type': 'timestamp', 'date': '2020-03-01 00:00:00'}
        今年三月        {'key': '今年3月', 'type': 'timestamp', 'date': '2020-03-01 00:00:00'}
        三月中旬        {'key': '3月15号', 'type': 'timestamp', 'date': '2020-03-15 00:00:00'}
        去年三月十五日  {'key': '去年3月15日', 'type': 'timestamp', 'date': '2019-03-15 00:00:00'}
        去年六月份      {'key': '去年6月', 'type': 'timestamp', 'date': '2019-06-01 00:00:00'}
        今天    {'key': '今天', 'type': 'timestamp', 'date': '2020-03-18 00:00:00'}
        昨天下午三点    {'key': '昨天下午3点', 'type': 'timestamp', 'date': '2020-03-17 15:00:00'}
        一个月后        {'key': '1个月后', 'type': 'timestamp', 'date': '2020-04-01 00:00:00'}
        明年    {'key': '明年', 'type': 'timestamp', 'date': '2021-01-01 00:00:00'}
        """


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
