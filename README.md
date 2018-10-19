# pyqthelloworld
[![Build Status](https://travis-ci.com/ericoporto/pyqthelloworld.svg?branch=master)](https://travis-ci.com/ericoporto/pyqthelloworld)

pyqt hello world!

## Why this?

I made so I could test building a snap from the [`snapcraft.yaml`](https://github.com/ericoporto/pyqthelloworld/blob/master/snap/snapcraft.yaml) below

    name: pyqthelloworld
    version: 0.1.0
    summary: pyqt hello world
    description: |
     a pyqt5 python3 hello world test
    grade: devel # must be 'stable' to release into candidate/stable channels
    confinement: strict # use 'strict' once you have the right plugs and slots

    apps:
      pyqthelloworld:
        command: desktop-launch $SNAP/bin/pyqthelloworld
        plugs:
        - desktop
        - desktop-legacy
        - unity7
        - wayland
        - x11
        - opengl

    parts:
      pyqthelloworld:
        after: [desktop-qt5]
        plugin: python
        python-version: python3
        source: git://github.com/ericoporto/pyqthelloworld
        source-type: git
        build-packages:
          - python3
          - python3-pyqt5
        stage-packages:
          - python3
          - python3-pyqt5
          - libc-bin
          - locales
