class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = 'softupload'
        self.UnzipMirrorCommand = 'extract'
        self.TarMirrorCommand = 'tarsoft'
        self.CancelMirror = 'cancel'
        self.CancelAllCommand = 'cancelall'
        self.ListCommand = 'find'
        self.StatusCommand = 'status'
        self.AuthorizedUsersCommand = 'users'
        self.deleteCommand = 'del'
        self.AuthorizeCommand = 'auth'
        self.UnAuthorizeCommand = 'unauth'
        self.AddSudoCommand = 'addsudo'
        self.RmSudoCommand = 'rmsudo'
        self.PingCommand = 'ping'
        self.RestartCommand = 'restart'
        self.StatsCommand = 'stats'
        self.HelpCommand = 'helpme'
        self.LogCommand = 'log'
        self.CloneCommand = "copy"
        self.WatchCommand = 'watch'
        self.TarWatchCommand = 'tarwatch'

BotCommands = _BotCommands()
