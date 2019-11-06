# markdown-captions

Converts images with alt text to `<figure>` with `<figcaption>`.

## Usage

```
pip install markdown-captions
```

``` python
md = markdown.Markdown(
    extensions=[
        'markdown_captions',
        'attr_list' # optional
    ]
)
```

## Examples

simple example
``` md
![caption](img.jpg)
![caption2](img2.jpg)
```
``` html
<p>
  <figure><img src="img.jpg" /><figcaption>caption</figcaption></figure>
  <figure><img src="img2.jpg" /><figcaption>caption2</figcaption></figure>
</p>
```

image title and class (with attr_list extension)
``` md
![caption](img.jpg "title"){: .class1 }
```
``` html
<figure class="class1"><img src="img.jpg" title="title" /><figcaption>caption</figcaption></figure>
```

inline captioned images
``` md
<style>
    .inline {
        display: inline-block;
    }
</style>
![caption](img.jpg){: .inline }
![caption2](img2.jpg){: .inline }
```
``` html
<p>
  <figure class="inline"><img src="img.jpg" /><figcaption>caption</figcaption></figure>
  <figure class="inline"><img src="img2.jpg" /><figcaption>caption2</figcaption></figure>
</p>
```

images with no alt text are not captioned
``` md
![](img.jpg)
```
``` html
<img src="img.jpg" />
```
