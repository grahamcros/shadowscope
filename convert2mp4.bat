for f in *.avi; do ffmpeg -i "${f}" "${f%%.*}.mp4; done
