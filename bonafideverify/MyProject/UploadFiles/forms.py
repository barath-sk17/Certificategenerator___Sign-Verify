from django import forms
class CreateForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'*Name of the Person', 'style':'width: 50%; padding: 12px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'}))
    roll=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'*Roll Number', 'style':'width: 50%; padding: 12px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'}))

class SignatureForm(forms.Form):
    studentroll=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'*Roll Number', 'style':'width: 50%; padding: 12px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'}))
    text_file=forms.FileField(widget=forms.FileInput(attrs={'style':'width: 50%; padding: 12px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'}))
    public_file=forms.FileField(widget=forms.FileInput(attrs={'style':'width: 50%; padding: 12px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'}))
    signature_file=forms.FileField(widget=forms.FileInput(attrs={'style':'width: 50%; padding: 12px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'}))    
