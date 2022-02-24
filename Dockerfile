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

RUN CHROME_VERSION=$(curl -sL https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    echo $CHROME_VERSION && \
    wget -q --continue -P /chromedriver/ "https://chromedriver.storage.googleapis.com/${CHROME_VERSION}/chromedriver_linux64.zip" && \
    unzip -o /chromedriver/chromedriver* -d /usr/local/bin/
RUN chmod 755 /usr/local/bin/chromedriver

RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt install -y /tmp/chrome.deb \
  && rm /tmp/chrome.deb

RUN FIREFOX_SETUP=firefox-setup.tar.bz2 && \
  apt-get purge firefox && \
  wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-latest&os=linux64" && \
  tar xjf $FIREFOX_SETUP -C /opt/ && \
  ln -s /opt/firefox/firefox /usr/bin/firefox && \
  rm $FIREFOX_SETUP

RUN apt-get install -y zip unzip
RUN apt-get install -y ffmpeg
COPY . /csol_automation_suite
ADD docker_entrypoint.sh /usr/bin/init_build_env
RUN chmod +x /usr/bin/init_build_env
ENTRYPOINT ["init_build_env"]
CMD ["bash"]
