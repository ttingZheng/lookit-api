# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-17 21:08
from __future__ import unicode_literals

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("accounts", "0040_add_message_model")]

    operations = [
        migrations.AddField(
            model_name="child",
            name="existing_conditions",
            field=bitfield.models.BitField(
                (
                    ("autism_spectrum_disorder", "Autism Spectrum Disorder"),
                    ("aspergers_syndrome", "Asperger's Syndrome"),
                    ("down_syndrome", "Down Syndrome"),
                    ("williams_syndrome", "Williams Syndrome"),
                    ("stroke", "Stroke"),
                    ("blind", "Blind"),
                    ("visual_impairment", "Visual Impairment"),
                    ("deaf", "Deaf"),
                    ("hearing_impairment", "Hearing Impairment"),
                    ("dyslexia", "Dyslexia"),
                    (
                        "attention_deficit_hyperactivity_disorder",
                        "Attention Deficit/Hyperactivity Disorder",
                    ),
                    ("learning_disability", "Learning Disability"),
                    ("generalized_anxiety_disorder", "Generalized Anxiety Disorder"),
                    ("obsessive_compulsive_disorder", "Obsessive-Compulsive Disorder"),
                    ("panic_disorder", "Panic Disorder"),
                    (
                        "post_traumatic_stress_disorder",
                        "Post-Traumatic Stress Disorder",
                    ),
                    (
                        "social_phobia_social_anxiety_disorder",
                        "Social Phobia/Social Anxiety Disorder",
                    ),
                    ("depression", "Depression"),
                    ("mood_disorder", "Mood Disorder"),
                    ("allergies", "Allergies"),
                    ("fetal_alcohol_syndrome", "Fetal Alcohol Syndrome"),
                    ("epilepsy", "Epilepsy"),
                ),
                default=0,
            ),
        ),
        migrations.AddField(
            model_name="child",
            name="languages_spoken",
            field=bitfield.models.BitField(
                (
                    ("cmn", "Mandarin"),
                    ("es", "Spanish"),
                    ("en", "English"),
                    ("hi", "Hindi"),
                    ("bn", "Bengali"),
                    ("pt", "Portuguese"),
                    ("ru", "Russian"),
                    ("ja", "Japanese"),
                    ("lah", "Western Punjabi"),
                    ("mr", "Marathi"),
                    ("te", "Telugu"),
                    ("wuu", "Wu"),
                    ("tr", "Turkish"),
                    ("ko", "Korean"),
                    ("fr", "French"),
                    ("de", "German"),
                    ("vi", "Vietnamese"),
                    ("ta", "Tamil"),
                    ("yue", "Yue"),
                    ("ur", "Urdu"),
                    ("jv", "Javanese"),
                    ("it", "Italian"),
                    ("egy", "Egyptian Spoken Arabic"),
                    ("gu", "Gujarati"),
                    ("pes", "Iranian Persian"),
                    ("bho", "Bhojpuri"),
                    ("nan", "Min Nan"),
                    ("hak", "Hakka"),
                    ("cjy", "Jinyu"),
                    ("ha", "Hausa"),
                    ("kn", "Kannada"),
                    ("id", "Indonesian"),
                    ("pl", "Polish"),
                    ("yo", "Yoruba"),
                    ("hsn", "Xiang Chinese"),
                    ("ml", "Malayalam"),
                    ("or", "Odia"),
                    ("mai", "Maithili"),
                    ("my", "Burmese"),
                    ("su", "Sunda"),
                    ("mor", "Moroccan Spoken Arabic"),
                    ("uk", "Ukrainian"),
                    ("ig", "Igbo"),
                    ("uzn", "Northern Uzbek"),
                    ("sd", "Sindhi"),
                    ("ro", "Romanian"),
                    ("tl", "Tagalog"),
                    ("nl", "Dutch"),
                    ("gan", "Gan"),
                    ("am", "Amharic"),
                    ("pbu", "Northern Pashto"),
                    ("mag", "Magahi"),
                    ("th", "Thai"),
                    ("skr", "Saraiki"),
                    ("km", "Khmer"),
                    ("hne", "Chhattisgarhi"),
                    ("so", "Somali"),
                    ("ms", "Malay"),
                    ("ceb", "Cebuano"),
                ),
                default=0,
            ),
        ),
        migrations.AddField(
            model_name="child",
            name="multiple_birth",
            field=bitfield.models.BitField(
                (
                    ("twin", "Twin"),
                    ("triplet", "Triplet"),
                    ("quadruplet", "Quadruplet"),
                    ("quintuplet", "Quintuplet"),
                    ("sextuplet", "Sextuplet"),
                    ("septuplet", "Septuplet"),
                    ("octuplet", "Octuplet"),
                ),
                default=0,
            ),
        ),
    ]
