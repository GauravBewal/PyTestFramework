FROM ubuntu:20.04

#Installing python
RUN apt update -y && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa  && \
    apt install python3.9 -y

RUN apt-get install -y wget
# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
#Updating apt to see and install Google Chrome
RUN apt-get -y update
RUN apt-get install -y python3-pip \
  libffi-dev \
  libssl-dev \
  curl \
  libcurl3-dev \
  libxml2-dev \
  libxslt-dev \
  libxrender1 \
  libasound2 \
  libdbus-glib-1-2 \
  libgtk-3-0 \
  xvfb \
  libffi-dev \
  libssl-dev

RUN apt-get -y update
#RUN apt-get install -y google-chrome-stable
RUN apt-get install -yqq unzip curl

RUN wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip" && \
    unzip /chromedriver/chromedriver* -d /usr/local/bin/
RUN chmod 755 /usr/local/bin/chromedriver

ARG CHROME_VERSION="90.0.4430.212-1"
RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
  && apt install -y /tmp/chrome.deb \
  && rm /tmp/chrome.deb
RUN FIREFOX_SETUP=firefox-setup.tar.bz2 && \
  apt-get purge firefox && \
  wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-latest&os=linux64" && \
  tar xjf $FIREFOX_SETUP -C /opt/ && \
  ln -s /opt/firefox/firefox /usr/bin/firefox && \
  rm $FIREFOX_SETUP

COPY . /csol_automation_suite/
WORKDIR /csol_automation_suite/

RUN chmod +x /csol_automation_suite/entrypoint.sh
CMD ["/csol_automation_suite/entrypoint.sh"]