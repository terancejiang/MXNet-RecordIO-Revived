#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Name: MXNet-RecordIO-Standalone
File Created: 2024/2/22 下午3:35
Author: Ying.Jiang
File Name: tester.py
"""

import os
import tempfile
import numpy as np
import mx_recordio as mx


def get_encode_data():
    mock_data = [
        np.random.rand(3, 3) for _ in range(5)
    ]
    # convert mock data to binary
    mock_data = [d.tobytes() for d in mock_data]

    headers = [
        mx.recordio.IRHeader(0, [np.random.random(size=10) for _ in range(10)], i, 0) for i in range(5)
    ]
    data = [mx.recordio.pack(headers[i], mock_data[i]) for i in range(5)]

    return data


#
def test_recordio_basic_functionality():
    mock_data = get_encode_data()
    # Setup: Create a temporary file
    _, temp_file_path = tempfile.mkstemp(suffix='.rec')
    # Step 1: Write Data
    record = mx.recordio.MXIndexedRecordIO('tmp.idx', 'tmp.rec', 'w')

    for i, item in enumerate(mock_data):
        record.write_idx(i, item)
    record.close()

    record = mx.recordio.MXIndexedRecordIO('tmp.idx', 'tmp.rec', 'r')
    # Step 2: Read Data and Verify
    for i, item in enumerate(mock_data):
        read_data = record.read_idx(i)
        expected_data = item
        assert read_data == expected_data, f"Data mismatch: expected {expected_data}, got {read_data}"

    # Cleanup: Remove temporary files
    os.remove("tmp.idx")
    os.remove('tmp.rec')

    print("Test passed: MXIndexedRecordIO basic functionality verified.")


if __name__ == "__main__":
    test_recordio_basic_functionality()
