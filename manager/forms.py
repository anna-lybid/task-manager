from django import forms


class WorkerSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Username/first name/last name"}),
    )


class PositionsSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Position name"}),
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Task name"}),
    )


class TaskOrderForm(forms.Form):
    sort_by = forms.MultipleChoiceField(
        choices=[("deadline", "Deadline"), ("priority", "Priority")],
        required=False,
        label="Sort by",
        widget=forms.CheckboxSelectMultiple(),
    )
    active_only = forms.BooleanField(
        required=False,
        label="Active tasks only",
        widget=forms.CheckboxInput(),
    )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Task type name"}),
    )
