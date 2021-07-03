from django.forms import ModelForm
from .models import FeaturedProduct


class FeaturedProductForm(forms.ModelForm):

  class Meta:
    model = FeaturedProduct
    fields = ['product', 'banner_image', 'title_text', 'special_text', 'explanation_text']

    labels = {
    'product': "Product", 
    'banner_image':"Banner Image", 
    'title_text':"Title Text", 
    'special_text':"Special Text", 
    'explanation_text':"Explanation Text"
    }

    help_texts = {
    'product': "Select a Product to feature on the Homepage", 
    'banner_image':"Select an Image for the Banner", 
    'title_text':"What is the name of the product? Example: New mens shirt design", 
    'special_text':"What makes this product appear here? Example 50 percent discount (Optional)", 
    'explanation_text':"Explain the product features. In less that 300 characters (Optional)"}