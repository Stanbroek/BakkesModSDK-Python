# Collection of python scripts for BakkesMod from Bakkes.

import bakkesmod
from bakkesmod import cvarManager, gameWrapper, Vector, Rotator

from random import randint


def airdribble(args):
    tut = gameWrapper.GetGameEventAsServer()

    player = tut.GetGameCar()
    ball = tut.GetBall()
    ballLoc = ball.GetLocation()

    distToBall = 400
    if ballLoc.Y > 0:
        distToBall = -distToBall

    destLocation = Vector(ballLoc.X - 50, ballLoc.Y - distToBall, 40)

    newRotNorm = ballLoc - destLocation
    newRotNorm.normalize()
    newRot = bakkesmod.VectorToRotator(newRotNorm)
    newRot.Pitch = 0  # Just want yaw
    newRotNorm.Z = 0
    player.Stop()

    player.SetLocation(destLocation)
    player.SetRotation(newRot)
    player.SetVelocity(Vector(400) * newRotNorm)

    ball.Stop()
    ball.SetLocation(Vector(ballLoc.X, ballLoc.Y, 100))

    newBallVel = Vector(500, 500, 0) * newRotNorm
    newBallVel.Z = 400
    ball.SetVelocity(newBallVel)


def airdribble2(args):
    if gameWrapper.IsInFreeplay():
        tut = gameWrapper.GetGameEventAsServer()
        player = tut.GetGameCar()
        ball = tut.GetBall()

        randomSpawnLoc = Vector(randint(-3800, 3800), randint(-4500, 4500), 35)
        goalNo = 0 if randomSpawnLoc.Y > 0 else 1  # determine which goal
        ballDest = tut.GenerateGoalAimLocation(goalNo, randomSpawnLoc)
        faceVec = ballDest - randomSpawnLoc
        faceVec.normalize()
        playerRot = bakkesmod.VectorToRotator(faceVec)

        player.Stop()
        player.SetLocation(randomSpawnLoc)
        player.SetRotation(playerRot)
        player.SetVelocity(Vector(500, 500, 0) * faceVec)

        ballLoc = randomSpawnLoc + Vector(250) * faceVec + Vector(0, 0, 53)
        ball.Stop()
        ball.SetLocation(ballLoc)
        # randint(*(choice([(-900, -500), (300, 500)])))
        ballVelocity = Vector(600) * faceVec + Vector(0, 0, 300)

        def shootBall(gw):
            ball.SetVelocity(ballVelocity)

        gameWrapper.SetTimeout(shootBall, .11)


def backwall(args):
    if gameWrapper.IsInFreeplay():
        tut = gameWrapper.GetGameEventAsServer()
        player = tut.GetGameCar()
        ball = tut.GetBall()

        ballSpawn = Vector(randint(-3261, 713), randint(-0, 2566), randint(18, 600))

        carSpawn = Vector(randint(-3777, -837), randint(-3891, -2946), 25)
        carSpawnRotation = Rotator(-100, randint(-23600, -9475), 0)
        ball.Stop()
        player.Stop()

        endLocation = Vector(randint(-3756, -983), randint(-5500, -4262), randint(600, 1900))

        if randint(0, 1) == 1:
            carSpawn.X = -carSpawn.X
            ballSpawn.X = -ballSpawn.X
            endLocation.X = -endLocation.X

        ball.SetLocation(ballSpawn)
        player.SetLocation(carSpawn)
        player.SetRotation(carSpawnRotation)
        velocity = tut.GenerateShot(ballSpawn, endLocation, randint(600, 1100))
        ball.SetVelocity(velocity)
        # player.SetVelocity(Vector)


def boom(args):
    tut = gameWrapper.GetGameEventAsServer()

    player = tut.GetGameCar()
    ball = tut.GetBall()
    shot = tut.GenerateShot(ball.GetLocation(), player.GetLocation(), 1300)

    def shootie(gw):
        ball.SetVelocity(shot)
        cvarManager.log("VEL X: " + str(shot.X) + ", Y:" + str(shot.Y) + ", Z:" + str(shot.Z))

    gameWrapper.SetTimeout(shootie, 1)


def catchies(args):
    ballVelocity = Vector(0)

    if gameWrapper.IsInFreeplay():
        tut = gameWrapper.GetGameEventAsServer()
        player = tut.GetGameCar()
        ball = tut.GetBall()

        playerStart = Vector(randint(-3000, 3300), randint(600, 3000), 65)
        playerStartRot = Rotator(0, randint(-32000, 32000), 0)
        player.Stop()
        player.SetLocation(playerStart)
        player.SetRotation(playerStartRot)

        ballStart = Vector(randint(-3000, 3300), -randint(600, 3000), randint(100, 1500))
        ball.Stop()
        ball.SetLocation(ballStart)

        # playerStartRot.Yaw -= 32000
        # playerStartRot.Roll = 0
        behind = bakkesmod.RotatorToVector(playerStartRot)

        behind.normalize()
        playerAwkwardSpot = playerStart - behind * Vector(randint(400, 600), randint(500, 800), randint(0, 200))
        player.SetVelocity(behind * Vector(800, 800, 0))

        ballVelocity = tut.GenerateShot(ballStart, playerAwkwardSpot, randint(700, 1000))

        def shootBall(gw):
            ball.SetVelocity(ballVelocity)

        gameWrapper.SetTimeout(shootBall, .3)


def ceilingshot(args):
    if gameWrapper.IsInFreeplay():
        tut = gameWrapper.GetGameEventAsServer()
        player = tut.GetGameCar()
        ball = tut.GetBall()

        xStart = randint(500, 1200) if randint(0, 1) == 1 else -randint(500, 1200)
        ballSpawn = Vector(xStart, randint(-1700, 1700), 95)
        ballSpawnNorm = Vector(ballSpawn.X, ballSpawn.Y, ballSpawn.Z)
        ballSpawnNorm.normalize()
        carSpawn = ballSpawn - (ballSpawnNorm * Vector(500, 100, 0)) - Vector(0, 0, 65)

        ball.Stop()
        player.Stop()
        ball.SetLocation(ballSpawn)
        player.SetLocation(carSpawn)

        distToBall = (ballSpawn - carSpawn)
        distToBall.normalize()
        carRot = bakkesmod.VectorToRotator(distToBall)
        player.SetRotation(carRot)
        ball.SetVelocity(distToBall * Vector(1200, 1200, 0))
        player.SetVelocity(distToBall * Vector(1200, 1200, 0))


def ceilingshot2(args):
    if gameWrapper.IsInFreeplay():
        tut = gameWrapper.GetGameEventAsServer()
        player = tut.GetGameCar()
        ball = tut.GetBall()

        xStart = randint(500, 1200) if randint(0, 1) == 0 else -randint(500, 1200)
        ballSpawn = Vector(xStart, randint(-1700, 1700), 95)
        ballSpawnNorm = Vector(ballSpawn.X, ballSpawn.Y, ballSpawn.Z)
        ballSpawnNorm.normalize()
        yDiff = xStart * 2 if randint(0, 1) == 0 else -xStart * 2
        carSpawn = ballSpawn - (ballSpawnNorm * Vector(500, 100, 0)) - Vector(0, max(-2000, min(yDiff, 2000)), 65)

        impact = ballSpawn - (ballSpawnNorm * Vector(500, 100, 0))

        ball.Stop()
        player.Stop()
        ball.SetLocation(ballSpawn)
        player.SetLocation(carSpawn)

        distToBall = (ballSpawn - impact)
        distToBall.normalize()
        carRot = bakkesmod.VectorToRotator(distToBall)
        player.SetRotation(carRot)
        ball.SetVelocity(distToBall * Vector(2200, 1200, 0))
        player.SetVelocity(distToBall * Vector(1200, 1200, 0))


def center(args):
    if gameWrapper.IsInFreeplay():
        tut = gameWrapper.GetGameEventAsServer()
        player = tut.GetGameCar()
        ball = tut.GetBall()

        xStart = randint(500, 1200) if randint(0, 1) == 0 else -randint(500, 1200)
        ballSpawn = Vector(xStart, randint(-1700, 1700), 95)
        ballSpawnNorm = Vector(ballSpawn.X, ballSpawn.Y, ballSpawn.Z)
        ballSpawnNorm.normalize()
        carSpawn = ballSpawn - (ballSpawnNorm * Vector(500, 100, 0)) - Vector(0, min(xStart * 2, 2000), 65)

        impact = ballSpawn - (ballSpawnNorm * Vector(500, 100, 0))

        ball.Stop()
        player.Stop()
        ball.SetLocation(ballSpawn)
        player.SetLocation(carSpawn)

        distToBall = (ballSpawn - impact)
        distToBall.normalize()
        carRot = bakkesmod.VectorToRotator(distToBall)
        player.SetRotation(carRot)
        ball.SetVelocity(distToBall * Vector(randint(2000, 3000), 1200, 0))
        player.SetVelocity(distToBall * Vector(1200, 1200, 0))


def dribble(args):
    if gameWrapper.IsInFreeplay():
        tut = gameWrapper.GetGameEventAsServer()
        player = tut.GetGameCar()
        ball = tut.GetBall()

        # xStart = randint(-1500, 1500) if randint(0, 1) is 1 else -randint(500, 1200)
        ballSpawn = Vector(randint(-1500, 1500), randint(-1700, 1700), 95)
        ballSpawnNorm = Vector(ballSpawn.X, ballSpawn.Y, ballSpawn.Z)
        ballSpawnNorm.normalize()

        # ballSpawnNorm*Vector(randint(300, 800), randint(300, 800), 0)
        carSpawn = ballSpawn - Vector(randint(300, 800), randint(300, 800), 65)

        ball.Stop()
        player.Stop()
        ball.SetLocation(ballSpawn)
        player.SetLocation(carSpawn)

        distToBall = (ballSpawn - carSpawn)
        distToBall.normalize()
        carRot = bakkesmod.VectorToRotator(distToBall)
        carRot.Yaw = carRot.Yaw + randint(-5000, 5000)

        player.SetRotation(carRot)

        velocity = Vector(randint(700, 1400), randint(700, 1400), 0)

        ball.SetVelocity(velocity)
        player.SetVelocity(velocity)


def tick(args):
    def callback(eventName):
        cvarManager.log("tick")
    gameWrapper.HookEvent('Function GameEvent_Soccar_TA.Active.Tick', callback)


def wallreads(args):
    ballVelocity = Vector(0)
    reverse = (randint(0, 1) == 1)
    if gameWrapper.IsInFreeplay():
        tut = gameWrapper.GetGameEventAsServer()
        player = tut.GetGameCar()
        ball = tut.GetBall()

        ballStart = Vector(randint(-3071, -843), randint(514, 3911), randint(100, 1700))

        playerStart = Vector(randint(-3300, -400), randint(-2800, -900), 25)
        playerStartRot = Rotator(0, randint(12760, 20760), 0)
        playerStartVel = Vector(0, randint(800, 2100), 0)

        if reverse:
            ballStart.X = -ballStart.X
            playerStart.X = -playerStartVel.X

        player.Stop()
        player.SetLocation(playerStart)
        player.SetRotation(playerStartRot)
        player.SetVelocity(playerStartVel)
        ball.Stop()
        ball.SetLocation(ballStart)

        # playerStartRot.Yaw -= 32000
        # playerStartRot.Roll = 0

        dest = Vector(randint(-4071, -2200), randint(1381, 2502), randint(1250, 1616))
        if reverse:
            dest.X = -dest.X

        ballVelocity = tut.GenerateShot(ballStart, dest, randint(1100, 1400))

        def shootBall(gw):
            ball.SetVelocity(ballVelocity)
            ball.SetAngularVelocity(Vector(randint(-5000, 5000), randint(-5000, 5000), randint(-5000, 5000)), False)

        gameWrapper.SetTimeout(shootBall, .3)


def onLoad():
    cvarManager.registerNotifier('py_airdribble', airdribble, 'desc', bakkesmod.PERMISSION_FREEPLAY)
    cvarManager.registerNotifier('py_airdribble2', airdribble2, 'desc', bakkesmod.PERMISSION_FREEPLAY)
    cvarManager.registerNotifier('py_backwall', backwall, 'desc', bakkesmod.PERMISSION_FREEPLAY)
    cvarManager.registerNotifier('py_boom', boom, 'desc', bakkesmod.PERMISSION_FREEPLAY)
    cvarManager.registerNotifier('py_catchies', catchies, 'desc', bakkesmod.PERMISSION_FREEPLAY)
    cvarManager.registerNotifier('py_ceilingshot', ceilingshot, 'desc', bakkesmod.PERMISSION_FREEPLAY)
    cvarManager.registerNotifier('py_ceilingshot2', ceilingshot2, 'desc', bakkesmod.PERMISSION_FREEPLAY)
    cvarManager.registerNotifier('py_center', center, 'desc', bakkesmod.PERMISSION_FREEPLAY)
    cvarManager.registerNotifier('py_dribble', dribble, 'desc', bakkesmod.PERMISSION_FREEPLAY)
    cvarManager.registerNotifier('py_tick', tick, 'desc', bakkesmod.PERMISSION_FREEPLAY)
    cvarManager.registerNotifier('py_wallreads', wallreads, 'desc', bakkesmod.PERMISSION_FREEPLAY)


def onUnload():
    gameWrapper.UnhookEvent('Function GameEvent_Soccar_TA.Active.Tick')
