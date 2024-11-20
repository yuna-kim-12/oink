from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Post, Comment
from .serializers import PostListSerializer, PostSerializer, PostDetailSerializer, CommentSerializer


@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def post_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    # 게시글 작성
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # 단일 게시글 조회
    if request.method == 'GET':
        # ??? F 오브젝트 활용할지 확인
        post.num_seen += 1
        post.save()
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
    
    if post.user == request.user:
        # 게시글 수정
        if request.method == 'PUT':
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)

        # 게시글 삭제
        elif request.method == 'DELETE':
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    # 게시글을 작성한 유저가 아닐 경우
    else:
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)



@permission_classes([IsAuthenticated])
@api_view(['POST'])
def like_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # 좋아요 취소
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    # 좋아요
    else:
        post.like_users.add(request.user)

    serializer = PostDetailSerializer(post)
    return Response(serializer.data)



@permission_classes([IsAuthenticated])
@api_view(['POST'])
def save_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # 저장 취소
    if request.user in post.save_users.all():
        post.save_users.remove(request.user)
    # 저장
    else:
        post.save_users.add(request.user)

    serializer = PostDetailSerializer(post)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # 댓글 생성
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if comment.user == request.user:
        # 댓글 삭제
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 댓글을 작성한 유저가 아닐 경우
    else:
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)