function linux_before_install()
{
    curl -L -o tools/travis/asis-gpl-2018-20180524-src.tar.gz \
https://community.download.adacore.com/v1/c338044768412af787c8cff13c0d952ed688df11?filename=asis-gpl-2018-20180524-src.tar.gz
    docker build --tag asis tools/travis/
}

function linux_script()
{
    umask og+w
    mkdir upload
    docker run -i -t -v$(pwd)/upload:/upload --user=max asis \
           /bin/bash -c \
 'spectool -R -g /src/asis.spec && \
  cp /src/* ~/rpmbuild/SOURCES/ && \
  rpmbuild -bb /src/asis.spec --define "_rpmdir /upload"'
}

${TRAVIS_OS_NAME}_$1
