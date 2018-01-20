function linux_before_install()
{
    docker build --tag gnatutil tools/travis/
}

function linux_script()
{
    umask og+w
    mkdir upload
    docker run -i -t -v$(pwd)/upload:/upload --user=max gnatutil \
           /bin/bash -c \
 'spectool -R -g /src/gnatutil.spec && \
  cp /src/*.patch ~/rpmbuild/SOURCES/ && \
  rpmbuild -bb /src/gnatutil.spec --define "_rpmdir /upload"'
}

${TRAVIS_OS_NAME}_$1
