from django.db import models

class Game(models.Model):
    FOOTBALL = 'FO'
    SOCCER = 'SO'
    BASEBALL = 'BA'
    HOCKEY = 'HO'
    TENNIS = 'TE'
    BASKETBALL = 'BS'

    SPORT_CHOICES = (
        (FOOTBALL, 'Football'),
        (SOCCER, 'Soccer'),
        (BASEBALL, 'Baseball'),
        (HOCKEY, 'Hockey'),
        (TENNIS, 'Tennis'),
        (BASKETBALL, 'Basketball')
    )

    sport = models.CharField(
        max_length=2,
        choices=SPORT_CHOICES,
        default=FOOTBALL,
    )

    teams = models.ManyToManyField('Team', related_name = "games")
    date = models.DateField(default = "1997-06-06")


    def __str__(self):
        return '%s' % (self.pk)


class Team(models.Model):

    FOOTBALL = 'FO'
    SOCCER = 'SO'
    BASEBALL = 'BA'
    HOCKEY = 'HO'
    TENNIS = 'TE'
    BASKETBALL = 'BS'

    SPORT_CHOICES = (
        (FOOTBALL, 'Football'),
        (SOCCER, 'Soccer'),
        (BASEBALL, 'Baseball'),
        (HOCKEY, 'Hockey'),
        (TENNIS, 'Tennis'),
        (BASKETBALL, 'Basketball')
    )

    sport = models.CharField(
        max_length=2,
        choices=SPORT_CHOICES,
        default=FOOTBALL,
    )

    name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50, null = True)
    league = models.CharField(max_length = 10, default = "nfl")


    def __str__(self):
        return '%s %s' % (self.city, self.name)


class Comment(models.Model):
    FACEBOOK = 'FB'
    TWITTER = 'TW'
    INSTAGRAM = 'IG'
    REDDIT = 'RE'

    MEDIA_OUTLET_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (INSTAGRAM, 'Instagram'),
        (REDDIT, 'Reddit')
    )

    media_outlet = models.CharField(
        max_length=2,
        choices=MEDIA_OUTLET_CHOICES,
        default=FACEBOOK,
    )
    game = models.ForeignKey('Game', null=True, on_delete = models.CASCADE)
    comment_text = models.CharField(max_length = 1000)
    team_to_win = models.ForeignKey('Team', null=True)
