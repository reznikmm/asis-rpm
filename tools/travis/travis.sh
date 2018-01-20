function linux_before_install()
{
    docker build --tag asis tools/travis/
}

function linux_script()
{
    umask og+w
    mkdir upload
    docker run -i -t -v$(pwd)/upload:/upload --user=max asis \
           /bin/bash -c \
 'spectool -R -g /src/asis.spec && \
  cp /src/*.diff ~/rpmbuild/SOURCES/ && \
  rpmbuild -bb /src/asis.spec --define "_rpmdir /upload"'
}

${TRAVIS_OS_NAME}_$1
