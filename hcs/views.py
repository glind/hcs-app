from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.detail import View
from django.urls import reverse_lazy
from .models import ScamReport
from .forms import ScamReportForm, ScamReportUpdateForm, ReportVoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.db.models import Count, Q


import requests

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


def homepage(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home_page.html')


class ScamReportListView(ListView):
    model = ScamReport
    template_name = 'scam_list.html'
    context_object_name = 'reports'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(up_vote_count=Count('reportvote__is_upvote', filter=Q(reportvote__is_upvote=True)))
        queryset = queryset.annotate(down_vote_count=Count('reportvote__is_upvote', filter=Q(reportvote__is_upvote=False)))
        return queryset

class ScamReportCreateView(CreateView):
    model = ScamReport
    form_class = ScamReportForm
    template_name = 'scam_create.html'
    success_url = reverse_lazy('list')

class ScamReportDetailView(DetailView):
    model = ScamReport
    template_name = 'scam_detail.html'
    context_object_name = 'report'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReportVoteForm()
        report = self.get_object()
        up_vote_count = report.reportvote_set.filter(is_upvote=True).count()
        down_vote_count = report.reportvote_set.filter(is_upvote=False).count()
        context['up_vote_count'] = up_vote_count
        context['down_vote_count'] = down_vote_count
        return context

class ScamReportUpdateView(UpdateView, LoginRequiredMixin):
    model = ScamReport
    form_class = ScamReportUpdateForm
    template_name = 'scam_update.html'
    context_object_name = 'report'
    success_url = reverse_lazy('list')

class ScamReportDeleteView(DeleteView):
    model = ScamReport
    template_name = 'scam_delete.html'
    success_url = reverse_lazy('list')
    context_object_name = 'report'


def vote_report(request, pk):
    report = get_object_or_404(ScamReport, pk=pk)

    if request.method == 'POST':
        form = ReportVoteForm(request.POST)
        try:
            if form.is_valid():
                vote = form.save(commit=False)
                vote.report = report
                vote.ip_address = request.META.get('REMOTE_ADDR')
                vote.save()
                return redirect('detail', pk=pk)
        except IntegrityError:
            # Handle the IntegrityError by redirecting back to the form
            # with an error message
            form.add_error(None, 'You have already voted.')
    else:
        form = ReportVoteForm()

    return render(request, 'scam_detail.html', {'report': report, 'form': form})