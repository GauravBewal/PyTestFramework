FROM packages.cyware.com/centos7:python3.9

COPY . /root/

WORKDIR /root/

RUN python3 -m venv venv
RUN source venv/bin/activate; pip install --upgrade pip; pip install -r requirements.txt

RUN chmod +x /root/entrypoint.sh
CMD ["/root/entrypoint.sh"]

