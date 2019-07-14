import unittest
from main import FileRecord, File, process_file

class TestFileMethods(unittest.TestCase):
    def test_read_records_malformed(self):
        # Call
        file = process_file('./test/malformed-file.log')

        # Assert
        self.assertEqual(len(file.records), 19)

    def test_read_records(self):
        # Call
        file = process_file('./test/test-file.log')

        # Assert
        self.assertEqual(len(file.records), 23)

    def test_read_empty_file(self):
        # Call
        file = process_file('./test/empty-file.log')

        # Assert 
        self.assertEqual(len(file.records), 0)

    def test_active_ips(self):
        # Setup
        records = [
            FileRecord('4.4.4.4', ''),
            FileRecord('5.5.5.5', ''),
            FileRecord('1.1.1.1', ''),
            FileRecord('1.1.1.1', ''),
            FileRecord('1.1.1.1', ''),
            FileRecord('1.1.1.1', ''),
            FileRecord('2.2.2.2', ''),
            FileRecord('2.2.2.2', ''),
            FileRecord('2.2.2.2', ''),
            FileRecord('3.3.3.3', ''),
            FileRecord('3.3.3.3', ''),
            FileRecord('3.3.3.3', ''),
        ]

        file = File(records)

        # Call
        top = file.active_ips(3)

        # Assert
        self.assertEqual(top[0][0], '1.1.1.1')
        self.assertEqual(top[1][0], '2.2.2.2')
        self.assertEqual(top[2][0], '3.3.3.3')

    def test_active_urls(self):
        # Setup
        records = [
            FileRecord('', 'GET /test/top4'),
            FileRecord('', 'GET /test/top5'),
            FileRecord('', 'GET /test/top1'),
            FileRecord('', 'GET /test/top1'),
            FileRecord('', 'GET /test/top1'),
            FileRecord('', 'GET /test/top1'),
            FileRecord('', 'GET /test/top2'),
            FileRecord('', 'GET /test/top2'),
            FileRecord('', 'GET /test/top2'),
            FileRecord('', 'GET /test/top3'),
            FileRecord('', 'GET /test/top3'),
            FileRecord('', 'GET /test/top3')
        ]

        file = File(records)

        # Call
        top = file.active_urls(3)

        # Assert
        self.assertEqual(top[0][0], 'GET /test/top1')
        self.assertEqual(top[1][0], 'GET /test/top2')
        self.assertEqual(top[2][0], 'GET /test/top3')

    def test_distinct_ips(self):
        # Setup
        records = [
            FileRecord('4.4.4.4', ''),
            FileRecord('5.5.5.5', ''),
            FileRecord('1.1.1.1', ''),
            FileRecord('1.1.1.1', ''),
            FileRecord('1.1.1.1', ''),
            FileRecord('1.1.1.1', ''),
            FileRecord('2.2.2.2', ''),
            FileRecord('2.2.2.2', ''),
            FileRecord('2.2.2.2', ''),
            FileRecord('3.3.3.3', ''),
            FileRecord('3.3.3.3', ''),
            FileRecord('3.3.3.3', ''),
        ]

        file = File(records)

        # Call
        distinct = file.distinct_ips()

        # Assert
        self.assertEqual(distinct, 5)

if __name__ == '__main__':
    unittest.main()