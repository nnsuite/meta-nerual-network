import os
from subprocess import Popen, PIPE

from oeqa.runtime.case import OERuntimeTestCase
from oeqa.core.decorator.oetimeout import OETimeout

class NNStreamerTest(OERuntimeTestCase):

    def test_nnstreamer(self):
        # unittest_common
        cmd = 'LD_LIBRARY_PATH=/usr/lib/gstreamer-1.0:$LD_LIBRARY_PATH ' \
        '/usr/lib/nnstreamer/unittest/unittest_common'
        (status, output) = self.target.run(cmd)
        msg = " NNSTREAMER UNITTEST FAILED ( unittest_common ): %s" % output
        self.assertEqual(status, 0, msg=msg)

        # unittest_sink
        cmd = 'LD_LIBRARY_PATH=/usr/lib/gstreamer-1.0:$LD_LIBRARY_PATH ' \
        '/usr/lib/nnstreamer/unittest/unittest_sink -d /usr/lib/nnstreamer/customfilters --gst-plugin-path=/usr/lib/gstreamer-1.0'
        (status, output) = self.target.run(cmd)
        msg = " NNSTREAMER UNITTEST FAILED ( unittest_sink ): %s" % output
        self.assertEqual(status, 0, msg=msg)

        # unittest_plugins
        cmd = 'LD_LIBRARY_PATH=/usr/lib/gstreamer-1.0:$LD_LIBRARY_PATH ' \
        'NNSTREAMER_SOURCE_ROOT_PATH=/usr/lib/nnstreamer/unittest ' \
        '/usr/lib/nnstreamer/unittest/unittest_plugins --gst-plugin-path=/usr/lib/gstreamer-1.0'
        (status, output) = self.target.run(cmd)
        msg = " NNSTREAMER UNITTEST FAILED ( unittest_plugins ): %s" % output
        self.assertEqual(status, 0, msg=msg)

        # unittest_src_iio
        cmd = 'LD_LIBRARY_PATH=/usr/lib/gstreamer-1.0:$LD_LIBRARY_PATH ' \
        '/usr/lib/nnstreamer/unittest/unittest_src_iio --gst-plugin-path=/usr/lib/gstreamer-1.0'
        (status, output) = self.target.run(cmd)
        msg = " NNSTREAMER UNITTEST FAILED ( unittest_src_iio ): %s" % output
        self.assertEqual(status, 0, msg=msg)

        # unittest_if
        cmd = 'LD_LIBRARY_PATH=/usr/lib/gstreamer-1.0:$LD_LIBRARY_PATH ' \
        '/usr/lib/nnstreamer/unittest/unittest_if --gst-plugin-path=/usr/lib/gstreamer-1.0'
        (status, output) = self.target.run(cmd)
        msg = " NNSTREAMER UNITTEST FAILED ( unittest_if ): %s" % output
        self.assertEqual(status, 0, msg=msg)

        # unittest_join
        cmd = 'LD_LIBRARY_PATH=/usr/lib/gstreamer-1.0:$LD_LIBRARY_PATH ' \
        '/usr/lib/nnstreamer/unittest/unittest_join --gst-plugin-path=/usr/lib/gstreamer-1.0'
        (status, output) = self.target.run(cmd)
        msg = " NNSTREAMER UNITTEST FAILED ( unittest_join ): %s" % output
        self.assertEqual(status, 0, msg=msg)

        # unittest_rate
        cmd = 'mkdir -p /usr/lib/nnstreamer/unittest/build/nnstreamer_example; '\
        'cp /usr/lib/nnstreamer/customfilters/* /usr/lib/nnstreamer/unittest/build/nnstreamer_example/; ' \
        'NNSTREAMER_SOURCE_ROOT_PATH=/usr/lib/nnstreamer/unittest ' \
        '/usr/lib/nnstreamer/unittest/unittest_rate; ' \
        'rm -rf /usr/lib/nnstreamer/unittest/build'
        (status, output) = self.target.run(cmd)
        msg = " NNSTREAMER UNITTEST FAILED ( unittest_rate ): %s" % output
        self.assertEqual(status, 0, msg=msg)

        # unittest_tizen_capi
        cmd = 'mkdir -p /usr/lib/nnstreamer/unittest/build/nnstreamer_example; ' \
        'cp /usr/lib/nnstreamer/customfilters/* /usr/lib/nnstreamer/unittest/build/nnstreamer_example/; ' \
        'LD_LIBRARY_PATH=/usr/lib/gstreamer-1.0:$LD_LIBRARY_PATH ' \
        'NNSTREAMER_SOURCE_ROOT_PATH=/usr/lib/nnstreamer/unittest ' \
        'NNSTREAMER_BUILD_ROOT_PATH=/usr/lib/nnstreamer/unittest/build ' \
        '/usr/lib/nnstreamer/unittest/unittest_tizen_capi --gst-plugin-path=/usr/lib/gstreamer-1.0; ' \
        'rm -rf /usr/lib/nnstreamer/unittest/build'
        (status, output) = self.target.run(cmd)
        msg = " NNSTREAMER UNITTEST FAILED ( unittest_tizen_capi ): %s" % output
        self.assertEqual(status, 0, msg=msg)

        # unittest_cppfilter
        cmd = 'LD_LIBRARY_PATH=/usr/lib/gstreamer-1.0:/usr/lib/nnstreamer/filters/:$LD_LIBRARY_PATH ' \
        '/usr/lib/nnstreamer/unittest/unittest_cppfilter --gst-plugin-path=/usr/lib/gstreamer-1.0'
        (status, output) = self.target.run(cmd)
        msg = " NNSTREAMER UNITTEST FAILED ( unittest_cppfilter ): %s" % output
        self.assertEqual(status, 0, msg=msg)

        # unittest_tizen_tensorflow_lite
        cmd = 'LD_LIBRARY_PATH=/usr/lib/gstreamer-1.0:$LD_LIBRARY_PATH ' \
        'NNSTREAMER_SOURCE_ROOT_PATH=/usr/lib/nnstreamer/unittest ' \
        '/usr/lib/nnstreamer/unittest/unittest_tizen_tensorflow_lite --gst-plugin-path=/usr/lib/gstreamer-1.0'
        (status, output) = self.target.run(cmd)
        msg = " NNSTREAMER UNITTEST FAILED ( unittest_tizen_tensorflow_lite ): %s" % output
        self.assertEqual(status, 0, msg=msg)

        # unittest_tizen_tensorflow_lite-set
        cmd = 'LD_LIBRARY_PATH=/usr/lib/gstreamer-1.0:$LD_LIBRARY_PATH ' \
        'NNSTREAMER_SOURCE_ROOT_PATH=/usr/lib/nnstreamer/unittest ' \
        '/usr/lib/nnstreamer/unittest/unittest_tizen_tensorflow_lite-set --gst-plugin-path=/usr/lib/gstreamer-1.0'
        (status, output) = self.target.run(cmd)
        msg = " NNSTREAMER UNITTEST FAILED ( unittest_tizen_tensorflow_lite-set ): %s" % output
        self.assertEqual(status, 0, msg=msg)

        # Do SSAT test
        cmd = 'export UNITTEST_DIR=/usr/lib/nnstreamer/unittest; '\
              'export CUSTOMLIB_DIR=/usr/lib/nnstreamer/customfilters; '\
              'export LD_LIBRARY_PATH=/usr/lib/gstreamer-1.0:$LD_LIBRARY_PATH; ' \
              'ln -s /usr/bin/python3 /usr/bin/python; '\
              'mkdir -p $UNITTEST_DIR/nnstreamer_filter_reload; ' \
              'cp $UNITTEST_DIR/unittest_filter_reload $UNITTEST_DIR/nnstreamer_filter_reload/; ' \
              'mkdir -p $UNITTEST_DIR/nnstreamer_repo_dynamicity; ' \
              'cp $UNITTEST_DIR/unittest_repo $UNITTEST_DIR/nnstreamer_repo_dynamicity; ' \
              'cd ${UNITTEST_DIR}/tests; '\
              'ssat'
        (status, output) = self.target.run(cmd)
        if not output.find('FAILED'):
            status = 0
        msg = " NNSTREAMER UNITTEST FAILED ( SSAT ): %s" % output
        self.assertEqual(status, 0, msg=msg)
