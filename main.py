from flask import Flask, render_template, jsonify
from subprocess import call
import libtorrent as lt
import time
app = Flask(__name__)

@app.route("/")
def play_torrent_view():
    return render_template('play_torrent.html')

@app.route("/torrent/<magnet_link>", methods=['GET'])
def torrent(magnet_link):
  ses = lt.session()
  params = {
    'save_path': './',
    'storage_mode': lt.storage_mode_t(2),
    'paused': False,
    'auto_managed': True,
    'duplicate_is_error': True
  }
  handle = lt.add_magnet_uri(ses, magnet_link, params)
  while (not handle.has_metadata()):
    time.sleep(.1)
  info = handle.get_torrent_info()
  file = lt.create_torrent(info)

  res = {
    'name': info.name()
  }
  return jsonify(**res)

@app.route("/play_torrent/<magnet_link>", methods=['POST'])
def play_torrent(magnet_link):
    cmd = 'peerflix "{}" --mpv'.format(magnet_link)
    print cmd
    call(cmd, shell=True)
    return 'asdasd'

if __name__ == "__main__":
    app.run()
