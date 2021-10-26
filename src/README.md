<nav class="navbar navbar-dark bg-primary bg-opacity-75">
<div class="container-fluid"><a class="navbar-brand" href="#">Static Site</a>
  <div class="dropdown">
      <button class="btn btn-warning dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
        Version
      </button>
      <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
        <li><a class="dropdown-item" href="#">0.1.0</a></li>
        <li><a class="dropdown-item" href="#">0.2.0</a></li>
        <li><a class="dropdown-item" href="#">0.3.0</a></li>
      </ul>
  </div>
</div>
</nav>

# Configuration Document

This must be the home page. Below are links to all sub pages.

1. [Getting Started](./01-GettingStarted/README.html)
1. [02-Parent2](./02-Parent2/README.html)


```{ .python use_pygments=true linenos=true title="An Example Code Block" } 

def fun1(a,b):
  print("yes")
  return true

page = Page()
fun1('./src/', './target/')

print("ok")

```

```{ .yaml use_pygments=true linenos=true title="Sample python"} 
parent:
  child: yes
  child2: no
```



<link href="./styles/style-gruvbox-light.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>