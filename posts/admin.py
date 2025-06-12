from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import (
    MusicModel, PostModel, LikeModel,
    CommentModel, CommentLikeModel,
    ReplyCommentModel, ReplyCommentLikeModel
)


# --------------------------ADMIN CUSTOMIZATIONS---------------------------

class BaseAdmin(admin.ModelAdmin):
    """Base admin class with common settings"""
    list_per_page = 25
    save_on_top = True
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')


# -----------------------------------------MODEL ADMINS------------------------------------

@admin.register(MusicModel)
class MusicModelAdmin(BaseAdmin):
    list_display = ('display_music', 'singer', 'created_at', 'updated_at')
    list_filter = ('singer', 'created_at')
    search_fields = ('music_name', 'singer__username')
    list_select_related = ('singer',)

    def display_music(self, obj):
        return f"🎵 {obj.music_name}"

    display_music.short_description = 'Music'


@admin.register(PostModel)
class PostModelAdmin(BaseAdmin):
    list_display = (
        'display_post', 'user_link', 'post_type',
        'music_link', 'likes_count', 'created_at'
    )
    list_filter = ('post_type', 'created_at', 'userID')
    search_fields = ('caption', 'hashtag', 'userID__username')
    raw_id_fields = ('userID', 'tagging', 'music')
    list_select_related = ('userID', 'music', 'music__singer')
    filter_horizontal = ()

    fieldsets = (
        ('Post Information', {
            'fields': ('userID', 'tagging', 'post_type', 'caption', 'hashtag')
        }),
        ('Media', {
            'fields': ('music', 'content_url'),
        }),
        ('Location', {
            'fields': ('address',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('wide',)
        }),
    )

    def display_post(self, obj):
        return format_html(
            '<span style="font-weight:600">{}</span>',
            obj.caption[:50] + '...' if len(obj.caption) > 50 else obj.caption
        )

    display_post.short_description = 'Post'

    def user_link(self, obj):
        url = reverse('admin:users_user_change', args=[obj.userID.id])
        return format_html('<a href="{}">{}</a>', url, obj.userID.username)

    user_link.short_description = 'User'

    def music_link(self, obj):
        url = reverse('admin:social_media_musicmodel_change', args=[obj.music.id])
        return format_html('<a href="{}">🎶 {}</a>', url, obj.music.music_name)

    music_link.short_description = 'Music'


@admin.register(LikeModel)
class LikeModelAdmin(BaseAdmin):
    list_display = ('id', 'post_link', 'user_link', 'created_at')
    list_filter = ('created_at', 'userID')
    search_fields = ('postID__caption', 'userID__username')
    raw_id_fields = ('postID', 'userID')

    def post_link(self, obj):
        url = reverse('admin:social_media_postmodel_change', args=[obj.postID.id])
        return format_html('<a href="{}">📌 {}</a>', url, obj.postID.caption[:30])

    post_link.short_description = 'Post'

    def user_link(self, obj):
        url = reverse('admin:users_user_change', args=[obj.userID.id])
        return format_html('<a href="{}">👤 {}</a>', url, obj.userID.username)

    user_link.short_description = 'User'


@admin.register(CommentModel)
class CommentModelAdmin(BaseAdmin):
    list_display = ('id', 'post_link', 'user_link', 'short_comment', 'created_at')
    list_filter = ('created_at', 'userID')
    search_fields = ('postID__caption', 'userID__username')
    raw_id_fields = ('postID', 'userID')

    def post_link(self, obj):
        url = reverse('admin:social_media_postmodel_change', args=[obj.postID.id])
        return format_html('<a href="{}">📌 {}</a>', url, obj.postID.caption[:30])

    post_link.short_description = 'Post'

    def user_link(self, obj):
        url = reverse('admin:users_user_change', args=[obj.userID.id])
        return format_html('<a href="{}">👤 {}</a>', url, obj.userID.username)

    user_link.short_description = 'User'

    def short_comment(self, obj):
        return obj.body[:50] + '...' if len(obj.body) > 50 else obj.body

    short_comment.short_description = 'Comment'


@admin.register(CommentLikeModel)
class CommentLikeModelAdmin(BaseAdmin):
    list_display = ('id', 'comment_link', 'user_link', 'created_at')
    list_filter = ('created_at', 'userID')
    search_fields = ('commentID__body', 'userID__username')
    raw_id_fields = ('commentID', 'userID')

    def comment_link(self, obj):
        url = reverse('admin:social_media_commentmodel_change', args=[obj.commentID.id])
        return format_html('<a href="{}">💬 {}</a>', url, obj.commentID.body[:30])

    comment_link.short_description = 'Comment'

    def user_link(self, obj):
        url = reverse('admin:users_user_change', args=[obj.userID.id])
        return format_html('<a href="{}">👤 {}</a>', url, obj.userID.username)

    user_link.short_description = 'User'


@admin.register(ReplyCommentModel)
class ReplyCommentModelAdmin(BaseAdmin):
    list_display = ('id', 'comment_link', 'user_link', 'short_reply', 'created_at')
    list_filter = ('created_at', 'userID')
    search_fields = ('commentID__body', 'userID__username')
    raw_id_fields = ('postID', 'userID', 'commentID')

    def comment_link(self, obj):
        url = reverse('admin:social_media_commentmodel_change', args=[obj.commentID.id])
        return format_html('<a href="{}">💬 {}</a>', url, obj.commentID.body[:30])

    comment_link.short_description = 'Original Comment'

    def user_link(self, obj):
        url = reverse('admin:users_user_change', args=[obj.userID.id])
        return format_html('<a href="{}">👤 {}</a>', url, obj.userID.username)

    user_link.short_description = 'User'

    def short_reply(self, obj):
        return obj.body[:50] + '...' if len(obj.body) > 50 else obj.body

    short_reply.short_description = 'Reply'


@admin.register(ReplyCommentLikeModel)
class ReplyCommentLikeModelAdmin(BaseAdmin):
    list_display = ('id', 'reply_link', 'user_link', 'created_at')
    list_filter = ('created_at', 'userID')
    search_fields = ('reply_commentID__body', 'userID__username')
    raw_id_fields = ('reply_commentID', 'userID')

    def reply_link(self, obj):
        url = reverse('admin:social_media_replycommentmodel_change', args=[obj.reply_commentID.id])
        return format_html('<a href="{}">↩️ {}</a>', url, obj.reply_commentID.body[:30])

    reply_link.short_description = 'Reply'

    def user_link(self, obj):
        url = reverse('admin:users_user_change', args=[obj.userID.id])
        return format_html('<a href="{}">👤 {}</a>', url, obj.userID.username)

    user_link.short_description = 'User'