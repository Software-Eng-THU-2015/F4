FROM python:2.7-onbuild

RUN apt-get update
RUN apt-get -y install python-setuptools
RUN apt-get -y install libmysqld-dev
RUN cd /usr/src/app
RUN git clone git://github.com/webpy/webpy.git
RUN ln -s `pwd`/webpy/web .
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["uwsgi", "--ini", "f4ss_uwsgi.ini"]