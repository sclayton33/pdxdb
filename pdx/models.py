from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list


# def get_histology_path(instance, filename):
#     return


class Pdx(models.Model):
    """
    Defines most required and desired info for a PDX model. Images are defined in another
    model and linked via ForeignKey.
    """

    # for more detailed info on each field, refer to the docs
    # model_id is primary key

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # patient info
    SEXES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('not specified', 'Not specified'),
    ]
    ETHNICITY_ASSESSMENT = [
        ('self assessed', 'Self assessed'),
        ('genetic data', 'Genetic data'),
    ]
    patient_id = models.CharField(max_length=200)
    patient_sex = models.CharField(max_length=13, choices=SEXES)
    patient_history = models.TextField(blank=True, null=True)
    patient_ethnicity = models.CharField(blank=True, null=True, max_length=100)
    ethnicity_assessment_method = models.CharField(blank=True, null=True, max_length=13, choices=ETHNICITY_ASSESSMENT)
    initial_diagnosis = models.TextField(blank=True, null=True)
    age_at_initial_diagnosis = models.PositiveIntegerField(blank=True, null=True)

    # patient tumor at collection time
    SHAREABLE = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    TREATMENT_NAIVE = [
        ('naive', 'Treatment naive'),
        ('not naive', 'Not treatment naive'),
        ('not specified', 'Not specified'),
    ]
    TREATED_OPTIONS = [
        ('Y', 'Yes'),
        ('N', 'No'),
        ('unknown', 'Unknown'),
    ]
    sample_id = models.CharField(max_length=250, unique=True)
    collection_date = models.DateField(blank=True, null=True)
    collection_event = models.CharField(blank=True, null=True, max_length=250)
    months_since_collection_one = models.PositiveIntegerField(blank=True, null=True)
    age_in_years_at_collection = models.PositiveIntegerField()
    diagnosis = models.TextField()
    diagnosis_notes = models.TextField(blank=True, null=True)
    tumor_type = models.CharField(max_length=100)
    primary_site = models.CharField(max_length=250)
    collection_site = models.CharField(max_length=250)
    stage = models.CharField(blank=True, null=True, max_length=30)
    staging_system = models.CharField(blank=True, null=True, max_length=250)
    grade = models.CharField(blank=True, null=True, max_length=30)
    grading_system = models.CharField(blank=True, null=True, max_length=250)
    virology_status = models.TextField(blank=True, null=True)
    treatment_info_shareable = models.CharField(max_length=3, choices=SHAREABLE)
    treatment_naive_at_collection = models.CharField(max_length=13, choices=TREATMENT_NAIVE)
    treated = models.CharField(max_length=13, choices=TREATED_OPTIONS)
    prior_treatment = models.CharField(max_length=13, choices=TREATED_OPTIONS)

    # PDX model details
    model_id = models.CharField(primary_key=True, max_length=100, unique=True)
    host_strain = models.CharField(max_length=250)
    host_strain_full = models.TextField()
    engraftment_site = models.CharField(max_length=250)
    engraftment_type = models.CharField(max_length=250)
    sample_type = models.CharField(max_length=250)
    sample_state = models.CharField(blank=True, null=True, max_length=250)
    passage_number = models.CharField(max_length=250, validators=[validate_comma_separated_integer_list])
    publications = models.TextField(blank=True, null=True)

    # PDX model validation
    validation_techniques = models.TextField()
    validation_description = models.TextField()
    passages_validated = models.CharField(max_length=250, validators=[validate_comma_separated_integer_list])
    validation_host_strain_full = models.TextField()

    # sharing and contact
    ACCESS_MODALITY = [
        ('transnational', 'Transnational access'),
        ('collaboration', 'Collaboration only'),
    ]
    provider_type = models.CharField(max_length=250)
    model_accessibility = models.CharField(max_length=250)
    europdx_access_modality = models.CharField(max_length=20, choices=ACCESS_MODALITY)
    contact_email = models.EmailField()
    contact_name = models.CharField(max_length=50)
    provider_name = models.CharField(max_length=50)
    provider_abbreviation = models.CharField(max_length=10)
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return self.model_id


# class HistologyImages(models.Model):
#
#     pdx = models.ForeignKey(Pdx, on_delete=models.CASCADE)
#     image = models.ImageField(max_length=100, blank=True, name=True)
