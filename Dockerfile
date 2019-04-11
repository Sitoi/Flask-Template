FROM sitoi/alpine-python:3.6
MAINTAINER SHI TAO <shitao0418@gmail.com>

LABEL io.k8s.description="Flask 项目模板（Flask Template）" \
    io.k8s.display-name="Flask 项目模板（Flask Template）" \
    io.openshift.expose-services="8000:http" \
    io.openshift.tags="builder,flask,template,docker"

WORKDIR /opt/app
ENV HOME /opt/app
ADD . /opt/app

RUN pip3 install -r requirements.txt --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple

USER 1001

EXPOSE 8000

ENTRYPOINT ["gunicorn"]
CMD ["-b 0.0.0.0:8000", "application:app"]