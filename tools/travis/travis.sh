function linux_before_install()
{
    docker build --tag libgpr tools/travis/
}

function linux_script()
{
    umask og+w
    mkdir upload
    docker run -i -t -v$(pwd)/upload:/upload --user=max libgpr \
           /bin/bash -c \
 'spectool -R -g /src/libgpr.spec && \
  rpmbuild -bb /src/libgpr.spec --define "_rpmdir /upload"'
}

${TRAVIS_OS_NAME}_$1
