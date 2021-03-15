from django import forms

class FormularioCurso(forms.Form): #describe como un formulario funciona y aparece en la web
    nombre = forms.CharField(label="Nombre", max_length=128)
    inscriptos = forms.IntegerField(label="Inscriptos")
    solo_empresas = forms.BooleanField(label="¿Solo empresas?", required=False) #va False porque es una casilla de verificacion, no debe aparecer tildada
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche")
    )
    turno = forms.ChoiceField(label="Turno", choices=TURNOS)
    fecha_inicio = forms.DateField(
        label = "Fecha de inicio", 
        widget=forms.DateInput(attrs={"type":"date"})
    )



