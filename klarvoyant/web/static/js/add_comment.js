window.addEvent('domready', function(){
    $$('.form_comment').hide();
    $$('.blog_comment').addEvent('click', function(e){
        this.hide();
        form_id = this.getParent().getElement('form').get('id');
        $(form_id).show();
    });
    $$('.comment_submit').addEvent('click', function(e) {
        this.getParent().getParent().getElement('.blog_comment').show();
        $(form_id).hide();
        form_id = this.getParent().get('id');
        var form_data = $(form_id).toQueryString();
        var url = '/blog/comment/add/'+form_id+'/';
        var comment_parent = this.getParent().getParent();
        var comments_div = comment_parent.getElement('.comments');
        var comments = comments_div.getElements('.comment');
        var ajaxRequest = new Request({ 
            url: url,
            method: 'POST',
            data: form_data,
            onSuccess: function(responseText){
                var new_comment = new Element('div', {
                    html: responseText,
                    'class': 'comment',
                });
                new_comment.inject(comments_div, 'top');
                if(comments.length > 2) {
                    comments[2].dispose();
                }

            }
        });
        ajaxRequest.send();
    });
     
});