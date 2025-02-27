from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from .models import Profile

def accept(request):
    if request.method == "POST":
        # Retrieve data from POST request
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        summary = request.POST.get("summary")
        degree = request.POST.get("degree")
        institution = request.POST.get("institution")
        graduation_year = request.POST.get("graduation_year")
        gpa = request.POST.get("gpa") or None  # Handle optional fields
        job_title = request.POST.get("job_title")
        company = request.POST.get("company")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date") or None  # Handle optional fields
        description = request.POST.get("description")
        skills = request.POST.get("skills")
        project_name = request.POST.get("project_name")
        project_description = request.POST.get("project_description")
        technologies = request.POST.get("technologies")
        project_link = request.POST.get("project_link") or None  # Handle optional fields
        certification = request.POST.get("certification")
        organization = request.POST.get("organization")
        completion_date = request.POST.get("completion_date")
        languages = request.POST.get("languages")

        # Create and save the Profile object
        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            address=address,
            summary=summary,
            degree=degree,
            institution=institution,
            graduation_year=int(graduation_year),
            gpa=float(gpa) if gpa else None,
            job_title=job_title,
            company=company,
            start_date=start_date,
            end_date=end_date,
            description=description,
            skills=skills,
            project_name=project_name,
            project_description=project_description,
            technologies=technologies,
            project_link=project_link,
            certification=certification,
            organization=organization,
            completion_date=completion_date,
            languages=languages,
        )
        profile.save()

        
         # Redirect to generate_cv view with profile_id parameter
        return redirect('generate_cv', profile_id=profile.id)
        

    # If not a POST request, render the form page
    return render(request, "home.html")


def generate_cv(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    
    # Render HTML template with profile data
    html_string = render_to_string('cv_template.html', {'profile': profile})
    
    # Generate PDF from HTML
    pdf_file = HTML(string=html_string).write_pdf()
    
    # Serve the file
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{profile.name}_CV.pdf"'
    return response


def download_cv(request, profile_id):
    # Retrieve the profile object
    profile = get_object_or_404(Profile, pk=profile_id)

    # Render the download_cv.html template with the profile data
    return render(request, 'download_cv.html', {'profile': profile})

def confirm_cv(request, profile_id):
    # Retrieve the profile object and render a confirmation page
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'confirm_cv.html', {'profile': profile})