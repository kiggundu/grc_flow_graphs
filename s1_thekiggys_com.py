#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: S1_Wavelets
# Author: Abraham Kiggundu
# Description: Wave sampling Level 1 denotational symbol source
# Generated: Sat Jun  6 22:35:11 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class s1_thekiggys_com(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "S1_Wavelets")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("S1_Wavelets")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "s1_thekiggys_com")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.windowing_factor = windowing_factor = 2
        self.samp_rate = samp_rate = 44000
        self.feature_size = feature_size = 8
        self.windows_per_resolution = windows_per_resolution = (samp_rate*(5/1000.0))/(feature_size*windowing_factor)
        self.resolution = resolution = 5

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/god/workspace/sdr-work/recordings/audio/6_5_2.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_probe_rate_1 = blocks.probe_rate(gr.sizeof_float*1, 500.0, 0.15)
        self.blocks_probe_rate_0 = blocks.probe_rate(gr.sizeof_float*1, 500.0, 0.15)
        self.blocks_message_debug_0_0 = blocks.message_debug()
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_float*1, feature_size*windowing_factor)
        self.blocks_add_xx_0 = blocks.add_vff(1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_probe_rate_0, 'rate'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.blocks_probe_rate_1, 'rate'), (self.blocks_message_debug_0_0, 'print'))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_probe_rate_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_deinterleave_0, 10), (self.blocks_add_xx_0, 10))
        self.connect((self.blocks_deinterleave_0, 11), (self.blocks_add_xx_0, 11))
        self.connect((self.blocks_deinterleave_0, 12), (self.blocks_add_xx_0, 12))
        self.connect((self.blocks_deinterleave_0, 2), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_deinterleave_0, 3), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_deinterleave_0, 4), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_deinterleave_0, 5), (self.blocks_add_xx_0, 5))
        self.connect((self.blocks_deinterleave_0, 6), (self.blocks_add_xx_0, 6))
        self.connect((self.blocks_deinterleave_0, 7), (self.blocks_add_xx_0, 7))
        self.connect((self.blocks_deinterleave_0, 8), (self.blocks_add_xx_0, 8))
        self.connect((self.blocks_deinterleave_0, 9), (self.blocks_add_xx_0, 9))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_probe_rate_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_deinterleave_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "s1_thekiggys_com")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_windowing_factor(self):
        return self.windowing_factor

    def set_windowing_factor(self, windowing_factor):
        self.windowing_factor = windowing_factor
        self.set_windows_per_resolution((self.samp_rate*(5/1000.0))/(self.feature_size*self.windowing_factor))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_windows_per_resolution((self.samp_rate*(5/1000.0))/(self.feature_size*self.windowing_factor))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_feature_size(self):
        return self.feature_size

    def set_feature_size(self, feature_size):
        self.feature_size = feature_size
        self.set_windows_per_resolution((self.samp_rate*(5/1000.0))/(self.feature_size*self.windowing_factor))

    def get_windows_per_resolution(self):
        return self.windows_per_resolution

    def set_windows_per_resolution(self, windows_per_resolution):
        self.windows_per_resolution = windows_per_resolution

    def get_resolution(self):
        return self.resolution

    def set_resolution(self, resolution):
        self.resolution = resolution


def main(top_block_cls=s1_thekiggys_com, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
