from __future__ import absolute_import, unicode_literals

import wagtail
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaHiddenInput

if wagtail.VERSION >= (2, 0):
    from wagtail.contrib.forms.forms import FormBuilder
else:
    from wagtail.wagtailforms.forms import FormBuilder


class WagtailCaptchaFormBuilder(FormBuilder):
    CAPTCHA_FIELD_NAME = 'wagtailcaptcha'

    @property
    def formfields(self):
        # Add wagtailcaptcha to formfields property
        fields = super(WagtailCaptchaFormBuilder, self).formfields
        fields[self.CAPTCHA_FIELD_NAME] = ReCaptchaField(label='', widget=ReCaptchaHiddenInput())

        return fields


def remove_captcha_field(form):
    form.fields.pop(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
    form.cleaned_data.pop(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
