## **PIXEL <span style="color:#ef5350">PAINTER</span>**

Ok, first of all, this script just gets all the pixels from the given image, builds an HTML table, and inserts each pixel obtained from the image into the table cells. So...with this in mind, from now on we will call the table cells: **Pixels**.

*For now this script is only executable from Windows.*

<span style="color:red">**IMPORTANT: The larger the image to be processed, the more pixels will be inserted in the HTML table, therefore it will take longer to load the file in the browser. Also handle the pixel size carefully.**</span>

**Install:**

pip install pixel-painter

**Usage:**

`pixelpainter -h` in cmd shows:

`usage: pixelpainter [-h] -i IMAGE [-ps PIXELSIZE] [-f FOLDER] [-m {save,copy}]`

`Script for convert images to HTML...Simple.`

`optional arguments:`
  `-h, --help            show this help message and exit`
  `-i IMAGE, --image IMAGE`
                        `Full path from image to process.`
  `-ps PIXELSIZE, --pixelsize PIXELSIZE`
                        `Pixel size.`
  `-f FOLDER, --folder FOLDER`
                        `Output folder to HTML file (in case from save argument)`
  `-m {save,copy}, --mode {save,copy}`
                        `Copy the generated code to clipboard (copy) or generate a HTML file (save).`

The only **required** argument is `-i`, the rest are optional and have default values:

| Argument    | Default value         |
| ----------- | :-------------------- |
| **-ps**     | 2                     |
| **-folder** | (Your Desktop folder) |
| **-mode**   | save                  |

**Comparison**:

|             16x16 image             |           Output HTML TABLE (Screenshot with zoom)           |
| :---------------------------------: | :----------------------------------------------------------: |
| ![](https://i.ibb.co/cgLt99x/1.png) | ![](https://i.ibb.co/6HnQMwF/2021-02-11-22-43-19-9d804bbbcdd7.png) |

**Output HTML Code Beautified with [this](https://www.freeformatter.com/html-formatter.html):**

```html
<style>
    #tabla {
    border-collapse:collapse;
    }
    #tabla td, th {
    padding:0;
    margin:0;
    width:5;
    height:5;
    }
</style>
<table id='tabla'>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#c1984a5c'></td>
        <td style='background-color:#c1984ac1'></td>
        <td style='background-color:#c1984aef'></td>
        <td style='background-color:#c1984aff'></td>
        <td style='background-color:#c1984aff'></td>
        <td style='background-color:#c1984aef'></td>
        <td style='background-color:#c1984ac1'></td>
        <td style='background-color:#c1984a5c'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#be954aa5'></td>
        <td style='background-color:#c7a25df9'></td>
        <td style='background-color:#e3ce9eff'></td>
        <td style='background-color:#f7eed2ff'></td>
        <td style='background-color:#fef9e7ff'></td>
        <td style='background-color:#fef9e7ff'></td>
        <td style='background-color:#f7eed2ff'></td>
        <td style='background-color:#e3ce9fff'></td>
        <td style='background-color:#c7a25df9'></td>
        <td style='background-color:#bf954aa5'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#bb924aa5'></td>
        <td style='background-color:#d7bd88ff'></td>
        <td style='background-color:#fbf4ddff'></td>
        <td style='background-color:#fff9deff'></td>
        <td style='background-color:#fff8d8ff'></td>
        <td style='background-color:#fff7d5ff'></td>
        <td style='background-color:#fff7d5ff'></td>
        <td style='background-color:#fff8d8ff'></td>
        <td style='background-color:#fff9deff'></td>
        <td style='background-color:#fbf4ddff'></td>
        <td style='background-color:#d7bd88ff'></td>
        <td style='background-color:#bb924aa5'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#b68f4a5c'></td>
        <td style='background-color:#c2a060f9'></td>
        <td style='background-color:#fbf3d6ff'></td>
        <td style='background-color:#fff6d2ff'></td>
        <td style='background-color:#ddd0a7ff'></td>
        <td style='background-color:#ddd0a7ff'></td>
        <td style='background-color:#fff6d1ff'></td>
        <td style='background-color:#fff6d2ff'></td>
        <td style='background-color:#ddd0a7ff'></td>
        <td style='background-color:#ddd0a7ff'></td>
        <td style='background-color:#fff6d2ff'></td>
        <td style='background-color:#fbf3d7ff'></td>
        <td style='background-color:#c29f60f9'></td>
        <td style='background-color:#b68f4a5c'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#b18a4ac1'></td>
        <td style='background-color:#deca9cff'></td>
        <td style='background-color:#fff6ccff'></td>
        <td style='background-color:#fff6ccff'></td>
        <td style='background-color:#7a5b2dff'></td>
        <td style='background-color:#7a5b2dff'></td>
        <td style='background-color:#fff6ccff'></td>
        <td style='background-color:#fff6ccff'></td>
        <td style='background-color:#7a5b2dff'></td>
        <td style='background-color:#7a5b2dff'></td>
        <td style='background-color:#fff6ccff'></td>
        <td style='background-color:#fff6cdff'></td>
        <td style='background-color:#dec99cff'></td>
        <td style='background-color:#b18b4ac1'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#ab854aef'></td>
        <td style='background-color:#f5e8c1ff'></td>
        <td style='background-color:#fff4c6ff'></td>
        <td style='background-color:#fff4c6ff'></td>
        <td style='background-color:#7a5b2dff'></td>
        <td style='background-color:#7a5b2dff'></td>
        <td style='background-color:#fff4c6ff'></td>
        <td style='background-color:#fff4c6ff'></td>
        <td style='background-color:#7a5b2dff'></td>
        <td style='background-color:#7a5b2dff'></td>
        <td style='background-color:#fff4c6ff'></td>
        <td style='background-color:#fff4c6ff'></td>
        <td style='background-color:#f5e8c1ff'></td>
        <td style='background-color:#ab864aef'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#a5814aff'></td>
        <td style='background-color:#fef3c2ff'></td>
        <td style='background-color:#fff3bfff'></td>
        <td style='background-color:#fff3c0ff'></td>
        <td style='background-color:#aa9667ff'></td>
        <td style='background-color:#aa9667ff'></td>
        <td style='background-color:#fff3c0ff'></td>
        <td style='background-color:#fff3c0ff'></td>
        <td style='background-color:#aa9667ff'></td>
        <td style='background-color:#aa9667ff'></td>
        <td style='background-color:#fff3c0ff'></td>
        <td style='background-color:#fff3c0ff'></td>
        <td style='background-color:#fef3c2ff'></td>
        <td style='background-color:#a5814aff'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#9f7d4aff'></td>
        <td style='background-color:#fef0b6ff'></td>
        <td style='background-color:#fff1b8ff'></td>
        <td style='background-color:#fceeb6ff'></td>
        <td style='background-color:#fff1b8ff'></td>
        <td style='background-color:#fff1b8ff'></td>
        <td style='background-color:#fff2b8ff'></td>
        <td style='background-color:#fff1b9ff'></td>
        <td style='background-color:#fff2b8ff'></td>
        <td style='background-color:#fff1b8ff'></td>
        <td style='background-color:#fcefb5ff'></td>
        <td style='background-color:#fff1b9ff'></td>
        <td style='background-color:#fef0b6ff'></td>
        <td style='background-color:#9f7c4aff'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#9a784aef'></td>
        <td style='background-color:#f5e3a2ff'></td>
        <td style='background-color:#fff0b1ff'></td>
        <td style='background-color:#d0b97aff'></td>
        <td style='background-color:#ffefb1ff'></td>
        <td style='background-color:#fff0b1ff'></td>
        <td style='background-color:#fff0b1ff'></td>
        <td style='background-color:#fff0b0ff'></td>
        <td style='background-color:#ffefb1ff'></td>
        <td style='background-color:#ffefb1ff'></td>
        <td style='background-color:#d0b97bff'></td>
        <td style='background-color:#fff0b1ff'></td>
        <td style='background-color:#f5e3a2ff'></td>
        <td style='background-color:#99784aef'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#93734ac1'></td>
        <td style='background-color:#dcc686ff'></td>
        <td style='background-color:#ffefa8ff'></td>
        <td style='background-color:#cbb170ff'></td>
        <td style='background-color:#b79b5aff'></td>
        <td style='background-color:#ddc784ff'></td>
        <td style='background-color:#f5e49fff'></td>
        <td style='background-color:#f5e49eff'></td>
        <td style='background-color:#ddc784ff'></td>
        <td style='background-color:#b79a5aff'></td>
        <td style='background-color:#cbb270ff'></td>
        <td style='background-color:#ffeea9ff'></td>
        <td style='background-color:#dcc586ff'></td>
        <td style='background-color:#93734ac1'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#8e6e4a5c'></td>
        <td style='background-color:#a48759f9'></td>
        <td style='background-color:#fbe698ff'></td>
        <td style='background-color:#fbe79eff'></td>
        <td style='background-color:#d1b873ff'></td>
        <td style='background-color:#ab8c4bff'></td>
        <td style='background-color:#937032ff'></td>
        <td style='background-color:#937032ff'></td>
        <td style='background-color:#ab8c4bff'></td>
        <td style='background-color:#d1b873ff'></td>
        <td style='background-color:#fbe79eff'></td>
        <td style='background-color:#fbe698ff'></td>
        <td style='background-color:#a4875af9'></td>
        <td style='background-color:#8e6e4a5c'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#896a4aa5'></td>
        <td style='background-color:#c8af71ff'></td>
        <td style='background-color:#fbe58fff'></td>
        <td style='background-color:#ffea97ff'></td>
        <td style='background-color:#ffeb9bff'></td>
        <td style='background-color:#ffeb9dff'></td>
        <td style='background-color:#ffeb9dff'></td>
        <td style='background-color:#ffeb9bff'></td>
        <td style='background-color:#ffea97ff'></td>
        <td style='background-color:#fbe58fff'></td>
        <td style='background-color:#c8ae71ff'></td>
        <td style='background-color:#896b4aa5'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#84674aa5'></td>
        <td style='background-color:#9c8057f9'></td>
        <td style='background-color:#d9c077ff'></td>
        <td style='background-color:#f7df86ff'></td>
        <td style='background-color:#fee789ff'></td>
        <td style='background-color:#fee789ff'></td>
        <td style='background-color:#f7df86ff'></td>
        <td style='background-color:#d9c177ff'></td>
        <td style='background-color:#9c8058f9'></td>
        <td style='background-color:#84674aa5'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#81644a5c'></td>
        <td style='background-color:#81644ac1'></td>
        <td style='background-color:#81644aef'></td>
        <td style='background-color:#81644aff'></td>
        <td style='background-color:#80644aff'></td>
        <td style='background-color:#81644aef'></td>
        <td style='background-color:#81644ac1'></td>
        <td style='background-color:#80654a5c'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
    </tr>
    <tr>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
        <td style='background-color:#00000000'></td>
    </tr>
</table>
```