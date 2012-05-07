from threading import Thread
from subprocess import Popen, PIPE, STDOUT


class PlaySound(Thread):
  def __init__(self, filename, volume):
    Thread.__init__(self)
    self.filename = filename
    self.volume = volume

  def run(self):
    cmd = 'play -v ' + self.volume + ' ' + self.filename
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
      stderr=STDOUT, close_fds=True)
    p.stdout.read()
