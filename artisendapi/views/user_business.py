import json
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from artisendapi.models import UserBusiness, Medium, Skill

class UserBusinessViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"error": "Authentication required"}, status=401)

        try:
            bio = request.data.get('bio', '')
            business_email = request.data.get('business_email', '')
            phone = request.data.get('phone', '')
            business_address = request.data.get('business_address', '')
            social_link = request.data.get('social_link', '')
            commissions_open = request.data.get('commissions_open', False)

            banner_img = request.FILES.get('banner_img')

            
            mediums_data = request.data.get('mediums', '[]')
            skills_data = request.data.get('skills', '[]')

            try:
                mediums_list = json.loads(mediums_data)
                skills_list = json.loads(skills_data)
            except json.JSONDecodeError:
                return Response({"error": "Invalid JSON for mediums or skills"}, status=400)

            business, created = UserBusiness.objects.get_or_create(user=user)

            business.bio = bio
            business.business_email = business_email
            business.phone = phone
            business.business_address = business_address
            business.social_link = social_link
            business.commissions_open = commissions_open

            if banner_img:
                business.banner_img = banner_img

            business.save()

            
            medium_objs = []
            for label in mediums_list:
                medium_obj, _ = Medium.objects.get_or_create(label=label)
                medium_objs.append(medium_obj)
            business.mediums.set(medium_objs)


            skill_objs = []
            for label in skills_list:
                skill_obj, _ = Skill.objects.get_or_create(label=label)
                skill_objs.append(skill_obj)
            business.skills.set(skill_objs)

            return Response({"success": True, "business_id": business.id}, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=500)