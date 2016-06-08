# pyqthelloworld
pyqt hello world!

## Why this?

I made so I could test building a snap from the file below

*snapcraft.yaml*

    name: pyqthelloworld
    version: 0.1.0
    summary: pyqt hello world
    description: |
     a pyqt5 python3 hello world test

    confinement: strict

    apps:
      pyqthelloworld:
        command: pyqthelloworld

    parts:
      pyqthelloworld:
        plugin: python3
        source: git://github.com/ericoporto/pyqthelloworld
        source-type: git
        stage-packages:
          - python3-pyqt5
          - libc-bin
          - locales
