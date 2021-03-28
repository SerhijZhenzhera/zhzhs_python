from django import forms


class CommentForm(forms.Form):
    nic_name = forms.CharField(max_length=25)
    comment_text = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        # return f"{self.comment_text} by {self.nic_name}"
        return self.comment_text, 'by', self.nic_name


class SearchBlog(forms.Form):
    blog_title = forms.CharField(max_length=25)

'''
class SearchAuthor(forms.Form):
    nic_name = forms.CharField(max_length=25)
'''
