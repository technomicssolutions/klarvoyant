
from sorl.thumbnail import get_thumbnail
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

def thumbnail(image_path):
        im = get_thumbnail(image_path, '200x200', quality=99)
        return u'<img style="border: 1px ridge #C0C0C0;" src="%s" alt="%s" />' % (im.url, image_path)

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            if name.endswith("video"):
                output.append(u' <a href="%s" target="_blank"><video width="200" height="200" controls="controls"><source src="{{ %s }}" alt="%s" s/></video></a> ' % \
                                                    (image_url, image_url, file_name))
            else:
                output.append(u' <a href="%s" target="_blank">%s</a>' % \
                (image_url, thumbnail(file_name)))
                
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
        
        
        
  