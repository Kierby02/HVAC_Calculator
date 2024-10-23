def calculate_hvac(request):
    if request.method == 'POST':
        building_size = float(request.POST.get('building_size'))
        insulation_rvalue = float(request.POST.get('insulation_rvalue'))
        climate_zone_factor = float(request.POST.get('climate_zone_factor'))
        num_occupants = int(request.POST.get('num_occupants'))
        
        total_load = (building_size * climate_zone_factor * insulation_rvalue) + (num_occupants * 500)

        tips = [
            "Use energy-efficient windows.",
            "Install proper insulation.",
            "Regular maintenance of HVAC system."
        ]
        
        return render(request, 'hvac_calculator.html', {
            'total_load': total_load,
            'tips': tips
        })
    return render(request, 'hvac_calculator.html')
