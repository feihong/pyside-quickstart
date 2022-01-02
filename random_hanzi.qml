import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import random_hanzi.signals.hanzi 1.0

ApplicationWindow {
  visible: true
  width: 800
  height: 600
  title: "Random Hanzi"

  Hanzi {
    id: hanzi
  }

  Shortcut {
    sequence: StandardKey.Quit
    context: Qt.ApplicationShortcut
    onActivated: Qt.quit()
  }

  ColumnLayout {
    anchors.fill: parent
    anchors.margins: 10

    Pane {
      Layout.fillHeight: true
      Layout.fillWidth: true

      Label {
        id: output
        anchors.centerIn: parent

        text: "你好"
        font.pixelSize: 40
      }
    }

    RowLayout {
      Layout.fillWidth: true

      Label {
        text: "Number of hanzi"
      }
      SpinBox {
        id: spinbox
        from: 1
        to: 100
        value: 8
      }
      Item {
        Layout.fillWidth: true
      }
      CheckBox {
        id: checkbox
        text: "Only show common hanzi"
      }
    }
    Button {
      Layout.fillWidth: true
      text: "Generate"
      onClicked: output.text = hanzi.random(spinbox.value, checkbox.checkState === Qt.Checked)
    }
  }
}
