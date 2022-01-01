# Feihong's PySide (Qt for Python) Quickstart

## Prerequisites

    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    # Update ~/.profile and ~/.bashrc according to instructions, then logout and login

    pyenv install --list # list all versions you can install
    pyenv install 3.10.1
    pyenv global 3.10.1

## Installation

    pip install --user pyside6

In order to install Qt Creator, you must create an account on the Qt website and [download the Qt Online Installer](https://www.qt.io/download-open-source).

## Commands

Run program

    python hello.py

Convert .ui file to Python source file

    pyside6-uic mainwindow.ui -o MainWindow.py

## Links

- [First steps with Qt Designer](https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/)
- [Create applications with QtQuick](https://www.pythonguis.com/tutorials/pyside6-qml-qtquick-python-application/)
- [Manual install of Qt 6](https://the-codeslinger.com/2020/12/20/manual-install-of-qt6-on-linux-mint/)

## Notes

I installed Qt to `~/opt/Qt`. Minimal Qt 6 installation with just Qt Design Studio selected takes up 3.3 GB. Don't bother installing CMake and Ninja through Qt online installer. You can add or remove Qt components using the Qt Maintenance Tool.
